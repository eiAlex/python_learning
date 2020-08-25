'''Ola meu amigo! om auxilio da biblioteca xmltodict disponível em [link][1]  é possível realizar o parser de xml para dict ou json e também realizar o caminho de volta.'''

#dependências
import xmltodict
import pprint
import json


my_xml = """
<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00">
	<NFe xmlns="http://www.portalfiscal.inf.br/nfe">
        <infNFe versao="4.00" Id="NFe35200823520039000135550010000031451090031450">
            <ide>
				<det nItem="1">
					<prod>
						<cProd>01.304</cProd>
						<cEAN>7898338312758</cEAN>
						<xProd>AF QUADRIAXIAL 6 QR6 HURRICANE</xProd>
						<NCM>85182100</NCM>
						<CEST>0105700</CEST>
					</prod>
				</det>
                <det nItem="2">
					<prod>
						<cProd>01.304</cProd>
						<cEAN>7898338312758</cEAN>
						<xProd>AF QUADRIAXIAL 6 QR6 HURRICANE</xProd>
						<NCM>85182100</NCM>
						<CEST>0105700</CEST>
					</prod>
				</det>
			</ide>
		</infNFe>
	</NFe>
</nfeProc>
"""
#parse
my_dict = xmltodict.parse(my_xml)

#dicionario
print(my_dict)

#acesso aos elementos do dicionário, para os que tem atributos se utiliza list:
print (my_dict['nfeProc']['NFe']['infNFe']['ide']['det'][0]['prod']['cEAN'])

#saída em json
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.dumps(my_dict))