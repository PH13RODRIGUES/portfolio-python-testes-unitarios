# portfolio-python-testes-unitarios
Projetos de testes unitários em Python: Calculadora Científica e Sistema de Descontos
# 🧪 Portfólio de Testes Unitários em Python

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/downloads/)
[![Pytest](https://img.shields.io/badge/Pytest-7.4.0-green?logo=pytest)](https://docs.pytest.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Tests](https://github.com/seu-usuario/portfolio-python-testes-unitarios/actions/workflows/tests.yml/badge.svg)](https://github.com/seu-usuario/portfolio-python-testes-unitarios/actions)

<div align="center">
  <img src="https://media.giphy.com/media/LMt9638dO8dftAjtco/giphy.gif" width="150" alt="Python Testing">
</div>

## 📌 Visão Geral
Dois projetos completos demonstrando **boas práticas de testes unitários** em Python:

| Projeto          | Descrição                          | Cobertura       |
|------------------|-----------------------------------|-----------------|
| [🧮 Calculadora Científica](/calculadora-cientifica) | Testes para operações matemáticas complexas | ![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen) |
| [🛍️ Sistema de Descontos](/sistema-descontos) | Testes de regras de negócio com edge cases | ![Coverage](https://img.shields.io/badge/Coverage-98%25-green) |

## 🚀 Como Executar

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/portfolio-python-testes-unitarios.git
cd portfolio-python-testes-unitarios

# Instalar dependências
pip install pytest pytest-cov

# Executar testes (em cada subpasta)
cd calculadora-cientifica
pytest -v --cov=.

📊 Métricas de Qualidade
✅ 100% de cobertura de testes na calculadora
✅ 98% de cobertura no sistema de descontos
✅ 0 warnings no pylint
✅ CI/CD integrado via GitHub Actions
