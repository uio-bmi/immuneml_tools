# immuneml_tools
Galaxy tool wrappers for immuneML. The tools rely on immuneML version 2.0.1 or newer.

https://immuneml.uio.no/

## Installation:
The tools can be installed from a Galaxy toolshed. You can also install them offline by editing Galaxy config files in the usual way.

### New datatype `immuneml_receptors.html`
No matter how you install the tools, you will need to define a new datatype, which is done as follows:

1. In your `galaxy.yml` look up the name of your `datatypes_config_file`. If the name is not yet defined, set
```
datatypes_config_file: datatypes_conf.xml
```
2. Make `datatypes_conf.xml` by copying `datatypes_conf.xml.sample` unless a `datatypes_config_file` was already defined.
3. Add the following line to your `datatypes_config_file`:
```
<datatype extension="immuneml_receptors.html" type="galaxy.datatypes.text:Html" subclass="True"/>
```
The line has to be inside `<registration>` along with the other datatypes.

### The immuneML package
Conda installation of immuneML typically takes several minutes. There is general information about Galaxy dependency resolution here: https://docs.galaxyproject.org/en/release_20.05/admin/conda_faq.html 

