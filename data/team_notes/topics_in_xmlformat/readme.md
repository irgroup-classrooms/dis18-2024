# XSD Documentation
XSD used to validate xml document.

## Validator
* OS: Linux (Debian, Arch)
* Validator: xmllint

## Code for validation
For the following Code, both files (xsd and xml) have to be in the same folder.

```bash
xmllint --schema topics_xml_validate.xsd topic_template_ALL.xml --noout
```
