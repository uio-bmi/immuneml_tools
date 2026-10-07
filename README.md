# immuneml_tools
Galaxy tool wrappers for immuneML. The tools rely on immuneML version 2.0.1 or newer.

https://immuneml.uio.no/

## Installation:
The tools can be installed from a Galaxy toolshed. You can also install them offline by editing Galaxy config files in the usual way.

### New immuneML datatypes
No matter how you install the tools, you will need to define the immuneML datatypes, which is done as follows:

1. In your `galaxy.yml` look up the name of your `datatypes_config_file`. If the name is not yet defined, set
```
datatypes_config_file: datatypes_conf.xml
```

2. Make `datatypes_conf.xml` by copying `datatypes_conf.xml.sample` unless a `datatypes_config_file` was already defined.

3. Add the following lines to your `datatypes_config_file`:
```
<datatype extension="immuneml_receptors.html" type="galaxy.datatypes.text:Html" subclass="True"/>
<datatype extension="immuneml_sequence.html" type="galaxy.datatypes.text:Html" subclass="True"/>
<datatype extension="immuneml_receptor.html" type="galaxy.datatypes.text:Html" subclass="True"/>
<datatype extension="immuneml_repertoire.html" type="galaxy.datatypes.text:Html" subclass="True"/>
```

The lines have to be inside `<registration>` along with the other datatypes.

The `immuneml_receptors.html` datatype is retained for backward compatibility and for tools where the dataset type cannot be determined before execution, such as tools using an arbitrary YAML specification.

The more specific datatypes allow Galaxy to distinguish between the following immuneML dataset types:

- `immuneml_sequence.html` - an immuneML sequence dataset containing individual TCR or BCR sequences.
- `immuneml_receptor.html` - an immuneML receptor dataset containing paired-chain TCR or BCR receptors.
- `immuneml_repertoire.html` - an immuneML repertoire dataset containing one or more repertoires, where each repertoire represents a set of TCR or BCR sequences from an individual or sample.

### The immuneML package
Conda installation of immuneML typically takes several minutes. There is general information about Galaxy dependency resolution here: https://docs.galaxyproject.org/en/release_20.05/admin/conda_faq.html
