from Bio import Entrez


class Organism:

    def __init__(self, id=None, term=None):
        self.id = id
        self.taxonomy = None
        self.rank = None
        self.name = None
        self.family = None
        self.genus = None
        self.order = None

        if term is None:
            self.set_taxonomy()
        else:
            self.set_taxonomy(term=term)

        if self.taxonomy is not None and len(self.taxonomy) > 0:
            self.set_properties()

    def set_taxonomy(self, term=None):
        """set the attribute taxonomy"""
        if term is not None:
            self.set_id(term)
        if self.id is not None:
            get_taxonomy = Entrez.efetch(db="Taxonomy", id=self.id, retmode="xml")
            self.taxonomy = Entrez.read(get_taxonomy)

    def set_properties(self):
        self.set_rank()
        self.set_name()
        self.set_genus()
        self.set_family()
        self.set_order()

    def set_rank(self):
        """set the attribute rank"""
        self.rank = self.taxonomy[0]["Rank"]

    def set_name(self):
        """set the attribute name"""
        self.name = self.taxonomy[0]["ScientificName"]

    def set_genus(self):
        """set the attribute genus"""
        lineage = self.taxonomy[0]["LineageEx"]
        genus = next((item for item in lineage if item["Rank"] == "genus"), None)
        if genus is not None:
            self.genus = genus["ScientificName"]
        if self.rank == "genus":
            self.genus = self.name

    def set_family(self):
        """set the attribute family"""
        lineage = self.taxonomy[0]["LineageEx"]
        family = next((item for item in lineage if item["Rank"] == "family"), None)
        if family is not None:
            self.family = family["ScientificName"]
        if self.rank == "family":
            self.family = self.name

    def set_order(self):
        """set the attribute order"""
        lineage = self.taxonomy[0]["LineageEx"]
        order = next((item for item in lineage if item["Rank"] == "order"), None)
        if order is not None:
            self.order = order["ScientificName"]
        if self.order == "order":
            self.order = self.name

    def set_id(self, term):
        """get the GenBank id of a Taxonomy"""
        request = Entrez.esearch(db="Taxonomy", term=term+"[ScientificName])", idtype="acc")
        result = Entrez.read(request)
        if result['Count'] == '1':
            self.id = result['IdList'][0]

