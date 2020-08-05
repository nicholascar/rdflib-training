from pyshacl import validate

r = validate("tenement-status.ttl", shacl_graph="ga-skos-profile-validator.ttl")
conforms, results_graph, results_text = r

print(conforms)
