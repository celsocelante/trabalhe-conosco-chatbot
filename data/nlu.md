## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- dont
- não
- cancela

## intent:inform_name
- sou (Igor)(name)
- sou [Igor](name) [Gadelha](surname)
- me chamo [claudio](name)
- me chamo [claudio](name) [santos](surname)
- [claudio](name) [santos](surname)
- [celso](name)
- [bruno](name)
- meu nome é [bruno](name)
- [Igor](name) [Gadelha](surname)

## intent:order
- quero um café
- quero um café [pequeno]({coffe_size})
- quero um café [médio]({coffe_size})
- quero um café [grande]({coffe_size})

## intent:inform_email
- [igor@gmail.com](email)
- [celso@hotmail.com.br](email)
- [bruno@comercio.br](email)

## intent:inform_cpf
- [999.999.999-99](cpf)
- [333.222.111-23](cpf)
- [123.223.098-35](cpf)

## regex:cpf
- /^\d{3}\.\d{3}\.\d{3}\-\d{2}$/

## regex:email
- [^@]+@[^@]+\.[^@]+
