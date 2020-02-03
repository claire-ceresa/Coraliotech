from Bio import Entrez
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from object.Organism import Organism
from object.CDS import CDS


class Protein:

    def __init__(self, id):

        self.id = id
        self.sequence = None
        self.name = None
        self.feature_cds = None
        self.feature_source = None
        self.feature_gene = None
        self.species = Organism()
        self.cds = CDS()
        self.molecular_weight = None
        self.is_predicted = False
        self.note = None

        self.set_sequence()
        self.set_features()
        self.set_species()
        self.set_name()
        self.set_cds()
        self.set_molecular_weight()
        self.set_is_predicted()
        self.set_notes()

        self._check_exception()

    def set_sequence(self):
        """set the attribute sequence with a SeqRecord object"""
        try:
            fiche = Entrez.efetch(db="nucleotide", id=self.id, rettype="gb", retmode="text")
        except:
            print(str(id) + " inconnu dans la base de donnees")
        else:
            self.sequence = SeqIO.read(fiche, "genbank")

    def set_features(self):
        """set the attributes concerning features"""
        self.set_feature_cds()
        self.set_feature_source()
        self.set_feature_gene()

    def set_species(self):
        """set the attribute species"""
        id = self.get_id_taxon()
        if id is not None:
            self.species = Organism(id)

    def set_name(self):
        """set the attribute name"""
        if self.feature_cds is not None and 'product' in self.feature_cds.qualifiers:
            self.name = self.feature_cds.qualifiers["product"][0]

    def set_cds(self):
        """set the attribute cds with a CDS Object"""
        if self.feature_cds is not None:
            start = self.feature_cds.location.start
            stop = self.feature_cds.location.end
            offset = int(self.feature_cds.qualifiers["codon_start"][0])
            if start is not None and stop is not None :
                self.cds = CDS(int(start+offset), int(stop), offset)

    def set_feature_cds(self):
        """set the attribute CDS feature"""
        if self.sequence is not None:
            self.feature_cds = self.get_feature_by_type("CDS")

    def set_feature_gene(self):
        """set the attribute gene feature"""
        if self.sequence is not None:
            self.feature_gene = self.get_feature_by_type("gene")

    def set_feature_source(self):
        """set the attribute source feature"""
        if self.sequence is not None:
            self.feature_source = self.get_feature_by_type("source")

    def set_molecular_weight(self):
        """set the attribute molecular weight"""
        translation = self.get_translation()
        if translation is not None:
            analysed_seq = ProteinAnalysis(translation)
            try:
                self.molecular_weight = round(analysed_seq.molecular_weight() * 0.001)
            except:
                return None

    def set_notes(self):
        """set the attribute note"""
        if self.feature_gene is not None:
            try:
                self.note = " ".join(self.feature_gene.qualifiers["note"])
            except Exception as e:
                print(e)

    def set_is_predicted(self):
        """set the boolean is_predicted"""
        if self.sequence is not None:
            self.is_predicted = "PREDICTED" in self.sequence.description

    def get_feature_by_type(self, type):
        """:param type: type of the feature you need (CDS, source, etc)
        :return: the object SeqFeature corresponding to the type"""
        for feature in self.sequence.features:
            if feature.type == type:
                return feature
        return None

    def get_translation(self):
        """:return the translation of the protein"""
        if self.feature_cds is not None and len(self.feature_cds.qualifiers["translation"]) > 0:
            translation = self.feature_cds.qualifiers["translation"][0]
            return translation
        return None

    def get_id_taxon(self):
        """:return the NCBI id of the taxon"""
        if self.feature_source is not None:
            id = self.feature_source.qualifiers["db_xref"][0].strip('taxon:')
            return int(id)
        return None

    def _check_exception(self):
        """check some precise exception and print a message if needed"""
        if self.cds.offset is not None and self.cds.offset > 1:
            print(str(self.id) + " : codon start > 1 --> verifier la taille du cds pour confirmation formule")

    def save_genbank_file(self):
        SeqIO.write(self.sequence, "fiche.txt", "genbank")

        # TO PRINT IT INTO PYQT
        # text_edit = QPlainTextEdit()
        # ...
        # text=open('file.txt').read()
        # text_edit.setPlainText(text)

