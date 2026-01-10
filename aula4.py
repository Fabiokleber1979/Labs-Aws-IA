#
import requests
def consultar_cep:(cep):
    cep = cep.replece("_","").strip()
    
    if len(cep) 