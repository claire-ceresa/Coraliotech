from Bio import Entrez
from object.Search import Search

Entrez.email = "claire.ceresa@hotmail.fr"

search = Search("Thalassianthidae", "Thalassianthidae AND mRNA[Title] AND complete[Title] AND cds[Title]", "mRNA complete cds")
