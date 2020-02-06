from Bio import Entrez


class Organism:

    def __init__(self, id=None):
        self.id = id
        self.taxonomy = None
        self.lineage = None
        self.species = None
        self.family = None
        self.genus = None
        self.order = None
        self.subclass = None
        self.classe = None
        self.phylum = None

        self.set_taxonomy()
        self.set_lineage()
        if self.taxonomy is not None and len(self.taxonomy) > 0:
            self.set_properties()

    def set_taxonomy(self):
        """set the attribute taxonomy"""
        if self.id is not None:
            get_taxonomy = Entrez.efetch(db="Taxonomy", id=self.id, retmode="xml")
            self.taxonomy = Entrez.read(get_taxonomy)

    def set_lineage(self):
        if self.taxonomy is not None:
            self.lineage = self.taxonomy[0]["LineageEx"]

    def set_properties(self):
        self.species = self.taxonomy[0]["ScientificName"]
        self.genus = next((item for item in self.lineage if item["Rank"] == "genus"), None)["ScientificName"]
        self.family = next((item for item in self.lineage if item["Rank"] == "family"), None)["ScientificName"]
        self.order = next((item for item in self.lineage if item["Rank"] == "order"), None)["ScientificName"]
        self.subclass = next((item for item in self.lineage if item["Rank"] == "subclass"), None)["ScientificName"]
        self.classe = next((item for item in self.lineage if item["Rank"] == "class"), None)["ScientificName"]
        self.phylum = next((item for item in self.lineage if item["Rank"] == "phylum"), None)["ScientificName"]
