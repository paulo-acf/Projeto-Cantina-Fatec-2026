Sistema de Cantina desenvolvido em Python com foco na aplicação de conceitos de Programação Orientada a Objetos (POO), organização modular e manipulação de dados. O projeto simula o funcionamento de uma cantina, permitindo o gerenciamento de produtos, controle de estoque, registro de vendas, acompanhamento de consumo e geração de relatórios.

A estrutura foi organizada em múltiplos módulos para separar responsabilidades, mantendo o código limpo e reutilizável. A classe principal `Sistema` centraliza as operações, sendo responsável por armazenar e manipular os dados internos da aplicação, como produtos, pagamentos e consumos. O sistema utiliza encapsulamento com atributos privados (duplo underline), garantindo maior controle e proteção dos dados.

Entre as principais funcionalidades, é possível cadastrar produtos com informações como nome, preço de compra, preço de venda, datas e quantidade em estoque. O sistema também permite realizar vendas, atualizando automaticamente o estoque, registrando pagamentos e armazenando o consumo. Além disso, há suporte para edição de quantidade com histórico de alterações, possibilitando rastrear modificações realizadas no estoque.

O projeto também implementa relatórios de vendas e consumo, além de avisos automáticos para produtos com estoque baixo ou vencidos. Para facilitar testes e simulações, é possível popular o sistema com dados aleatórios utilizando a biblioteca Faker.

Outro recurso importante é a persistência de dados com o uso do módulo pickle, permitindo salvar e carregar o estado completo do sistema. Também foi implementada a geração de relatórios em PDF, reunindo informações de vendas, consumo, estoque e avisos em um único documento simples e apresentável.

Este projeto atende aos requisitos de criação de estruturas próprias e separação de responsabilidades, servindo como base para estudos de POO, organização de código em Python e desenvolvimento de sistemas simples de gerenciamento.
