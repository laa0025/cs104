{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPKl5UU00zZTkHa/c4DnF+6",
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
        "<a href=\"https://colab.research.google.com/github/laa0025/cs104/blob/main/lab3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V2tCagBFMNm1",
        "outputId": "9265efad-f556-445e-92d7-16e3a35ddbd8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter cipher shift: 67\n",
            "Enter message: hi\n",
            "Encrypted message: LM\n",
            "Decrypted message: hi\n"
          ]
        }
      ],
      "source": [
        "shift = int(input(\"Enter cipher shift: \"))\n",
        "message = input(\"Enter message: \")\n",
        "\n",
        "MIN_ASCII = 32\n",
        "MAX_ASCII = 126\n",
        "RANGE = 95\n",
        "\n",
        "\n",
        "def encrypt(text, shift):\n",
        "    encrypted = \"\"\n",
        "\n",
        "    for char in text:\n",
        "        if char == \"\\n\" or char == \"\\t\":\n",
        "            encrypted += char\n",
        "        else:\n",
        "            ascii_code = ord(char)\n",
        "            new_code = MIN_ASCII + ((ascii_code - MIN_ASCII + shift) % RANGE)\n",
        "            encrypted += chr(new_code)\n",
        "\n",
        "    return encrypted\n",
        "\n",
        "\n",
        "def decrypt(text, shift):\n",
        "    decrypted = \"\"\n",
        "\n",
        "    for char in text:\n",
        "        if char == \"\\n\" or char == \"\\t\":\n",
        "            decrypted += char\n",
        "        else:\n",
        "            ascii_code = ord(char)\n",
        "            new_code = MIN_ASCII + ((ascii_code - MIN_ASCII - shift) % RANGE)\n",
        "            decrypted += chr(new_code)\n",
        "\n",
        "    return decrypted\n",
        "\n",
        "\n",
        "encrypted_message = encrypt(message, shift)\n",
        "decrypted_message = decrypt(encrypted_message, shift)\n",
        "\n",
        "print(\"Encrypted message:\", encrypted_message)\n",
        "print(\"Decrypted message:\", decrypted_message)"
      ]
    }
  ]
}