# How to use autogen_python.py

## Command line arguments 

This module needs one command line argument. This argument should be a **relative path** to the INI file used for the autogen process.

Example:
```
python ..\..\..\Codegen\Codegen_Python\autogen_python.py autogen_python_config.ini
```

## The INI file content

The INI file must have the following structure:
```
[System]
; e.g. BR12
system = BR12

[Paths]
; Note!!! Space between commas are not allowed
; Note!!! Always use forward slashes to be compatible with Windows and Linux
; Note!!! Items are allowed to span over multiple lines provided one level of indentation is used
; "acPath" (string)-> The relative path to the XML file
xml_path = [
    {"acPath":"../../../SICD/RMS_HMI_CONTROL_Msg.xml"},
    {"acPath":"../../../SICD/RMS_DEU_Msg.xml"}
    ]
; e.g. autogen_output_path = ../Autogen/
autogen_output_path = ../Autogen/
; e.g. template_path = ./FileTypeDefinitionsH.template
template_message_define_path = ../../../Codegen/Codegen_Python/python.message.define.j2
py_types_path = ../../../Codegen/Codegen_Base_Files/CCS_Types.py
```

There must be two sections namely **System** and **Paths**. The system section must contain the name of the system for which code is being generated. **All paths must be relative and not absolute.** Paths to files and directories in the INI file is relative to the directory where python is called from. 

The "Paths" section must contain:

Field                            | Description
---------------------------------|----------
xml_path                         | A JSON string containing a list of XML file to parse. For each XML file we supply a path, a boolean flag indicating if the XML file is a primary, a boolean flag indicating if the XML file is for an RMS handler or an interace and a MQTT QOS level. Note! make sure there are no spaces between commas!!!
autogen_output_path              | The relative path where the output should be generated to.
template_path                    | The relative path to the Jinja template used for Python class generation.
py_types_path                    | The relative path to directory containing the CCS base files.

In the **Paths** section JSON field **xml_path** must have the following keys:
Key                                      |  Type          | Description
-----------------------------------------|----------------|--------------
acPath                                   | Required       | The relative path of the XML file



The semicolons are used for comments and will not be parsed.

## Troubleshooting

The module also generates a log file in order to troubleshoot if needed. The log file will be saved to the working directory from which the python module was called. The log file should be examined if the autogen process did not complete successfully. Entries marked as "ERROR" should be considered first when fault finding.

## Suggested usage of the autogen

It is suggested when creating a new program which will make use of the autogen to have the following directory structure:
```
New_Program\
╠═══Autogen\
╠═══Codegen\
╠═══════generate.bat
╠═══════autogen_python_config.ini
╠═══Source\
╠═══════new_program.py
```

## Debugging the autogen Python code with VSCode

Using VSCode open the rms/Codegen/Codegen_Python folder. The launch.json file is already set up for the pupose of debugging with the "args" field set to ["autogen_python_config.ini"]

## Autogen limitations

* All messages must have a payload section if it is empty.
* Header fields cannot have enumerations as default values.
* Structures (Typedef with Records) must have at least 2 fields.
* Enums (Typedef with a record and enumerations inside) must have at least 2 enumerations.
