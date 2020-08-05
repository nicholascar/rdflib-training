from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:7200/repositories/training2")
q = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    
    SELECT ?cs ?pl
    WHERE {
        ?cs a skos:ConceptScheme ;
            skos:prefLabel ?pl .
    }
    ORDER BY ?pl
    """
sparql.setQuery(q)
sparql.setReturnFormat(JSON)
r = sparql.queryAndConvert()

import pprint
pprint.pprint(r)
