Installation
============
You will need to define a new datatype ``immuneml_receptors``, which is done as follows:

1. In your ``galaxy.yml`` look up the name of your ``datatypes_config_file``. If the name is not yet defined, set

``datatypes_config_file: datatypes_conf.xml``

2. Make ``datatypes_conf.xml`` by copying ``datatypes_conf.xml.sample`` unless a ``datatypes_config_file`` was already defined.
3. Add the following line to your ``datatypes_config_file``:

``<datatype extension="immuneml_receptors" type="galaxy.datatypes.text:Html" subclass="True"/>``
The line has to be inside ``<registration>`` along with the other datatypes.

The immuneML conda package
==========================
Galaxy will need to install the immuneML conda package. This conda installation typically takes several minutes. 
