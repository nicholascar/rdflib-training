from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, SKOS, XSD

g = Graph()
# loading a local file
# g.parse("bdm.ttl", format="turtle")
# g.serialize("bdm.xml")

# print length of the graph (no. triples)
# print(len(g))

# for s, p, o in g.triples((None, None, None)):
#     print(p)

# # getting each Concept in the graph
# for s, p, o in g.triples((None, RDF.type, SKOS.Concept)):
#     # getting the prefLabels for each Concept
#     for s2, p2, o2 in g.triples((s, SKOS.prefLabel, None)):
#         if "Core" in str(o2):
#             print(s, o2)

# # doing the above task using SPARQL
# q = """
#     PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
#
#     SELECT ?uri ?pl
#     WHERE {
#         ?uri rdf:type skos:Concept .
#         ?uri skos:prefLabel ?pl .
#
#         FILTER REGEX(?pl, "Core")
#     }
#     ORDER BY ?pl
#     """
# for r in g.query(q):
#     print(str(r["uri"]), str(r["pl"]))
#
# namespaces in serialization
EG = Namespace("http://example.com/")
g.bind("eg", EG)
# data = """
#         <http://example.com/p1> a <http://example.com/Person> .
#         <http://example.com/p1> <http://example.com/name> "Nick"@en .
#         <http://example.com/p1> <http://example.com/name> "Mikolajek"@pl .
#         """
# g.parse(data=data, format="turtle")

# create triple by triple
g.add((
    URIRef("http://example.com/p1"),    # subject
    RDF.type,                           # predicate, same as 'a'
    URIRef("http://example.com/Person")
))
g.add((URIRef("http://example.com/p1"), URIRef("http://example.com/name"), Literal("Nick", lang="en")))
g.add((
    EG.p1,
    EG.name,
    Literal("Mikolajek", lang="pl")
))
g.remove((
    EG.p1,
    EG.name,
    Literal("Mikolajek", lang="pl")
))

g2 = Graph()
g2.add((
    EG.p1,
    EG.birthdate,
    Literal("1982-05-11", datatype=XSD.date)
))
g2.add((
    EG.p1,
    EG.age,
    Literal("38", datatype=XSD.integer)
))

g3 = g + g2

print(g3.serialize(format="turtle").decode())

# parse data from the web
# g.parse(location="http://pid.geoscience.gov.au/sample/AU1000005?_view=igsn-o&_format=text/turtle")
# print(g.serialize(format="turtle").decode())
