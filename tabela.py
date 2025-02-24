{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPFSz0Euki8kRYQ7qId2+mC",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/luzagoc/HTML-CSS/blob/main/tabela.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4QvtnTw3ct6H",
        "outputId": "71e7d561-5f7b-43c9-c939-a190d63cceb8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o nome: SDHGADH\n",
            "Digite a data (formato DD/MM/AAAA): 2753425\n",
            "Digite o nome: GDJAGFDJ\n",
            "Digite a data (formato DD/MM/AAAA): 4383586\n",
            "Digite o nome: DAFJSD\n",
            "Digite a data (formato DD/MM/AAAA): 8538\n",
            "Digite o nome: WRTUW\n",
            "Digite a data (formato DD/MM/AAAA): 35683586\n",
            "Digite o nome: SFGJS\n",
            "Digite a data (formato DD/MM/AAAA): 6549354\n",
            "Nomes e Datas cadastrados:\n",
            "+----------+----------+\n",
            "|   Nome   |   Data   |\n",
            "+----------+----------+\n",
            "| SDHGADH  | 2753425  |\n",
            "| GDJAGFDJ | 4383586  |\n",
            "|  DAFJSD  |   8538   |\n",
            "|  WRTUW   | 35683586 |\n",
            "|  SFGJS   | 6549354  |\n",
            "+----------+----------+\n"
          ]
        }
      ],
      "source": [
        "from prettytable import PrettyTable\n",
        "\n",
        "tabela = PrettyTable([\"Nome\", \"Data\"])\n",
        "\n",
        "for i in range(5):\n",
        "    nome = input(\"Digite o nome: \")\n",
        "    data = input(\"Digite a data (formato DD/MM/AAAA): \")\n",
        "    tabela.add_row([nome, data])\n",
        "\n",
        "print(\"Nomes e Datas cadastrados:\")\n",
        "print(tabela)"
      ]
    }
  ]
}