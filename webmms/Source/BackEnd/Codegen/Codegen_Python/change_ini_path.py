import configparser as ConfigParser
import os

def change_ini(xml, systemName, xmlSchema):
    config = ConfigParser.RawConfigParser()
    config.optionxform = str
    config.read(os.path.join(os.path.dirname(__file__),"autogen_python_config.ini"), encoding=None)
    config.set('System', 'system', systemName)
    config.set('System', 'schema_format', xmlSchema)
    config.set('Paths', 'xml_path', '[{"acPath":"../../SICD/'+xml+'"}]' )
    with open(os.path.join(os.path.dirname(__file__),"autogen_python_config.ini"), 'w') as configfile:
        config.write(configfile)
        configfile.flush()
    configfile.close()
    