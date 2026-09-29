{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO8DCqfnihvi37XAqq9zHDB",
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
        "<a href=\"https://colab.research.google.com/github/laa0025/cs104/blob/main/lab4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "B6Il9_rbWVV7"
      },
      "outputs": [],
      "source": [
        "def score_to_letter(score):\n",
        "    if score >= 90:\n",
        "        return \"A\"\n",
        "    elif score >= 80:\n",
        "        return \"B\"\n",
        "    elif score >= 70:\n",
        "        return \"C\"\n",
        "    elif score >= 60:\n",
        "        return \"D\"\n",
        "    else:\n",
        "        return \"F\"\n",
        "\n",
        "\n",
        "students = []\n",
        "\n",
        "num_students = int(input(\"How many students? \"))\n",
        "\n",
        "while num_students < 5:\n",
        "    print(\"You must enter at least 5 students.\")\n",
        "    num_students = int(input(\"How many students? \"))\n",
        "\n",
        "for i in range(num_students):\n",
        "    name = input(f\"Enter student {i + 1} name: \")\n",
        "    score = float(input(f\"Enter {name}'s grade (0-100): \"))\n",
        "\n",
        "    while score < 0 or score > 100:\n",
        "        print(\"Grade must be between 0 and 100.\")\n",
        "        score = float(input(f\"Enter {name}'s grade (0-100): \"))\n",
        "\n",
        "    letter = score_to_letter(score)\n",
        "    students.append((name, score, letter))\n",
        "\n",
        "total = 0\n",
        "\n",
        "for name, score, letter in students:\n",
        "    total += score\n",
        "\n",
        "average = total / len(students)\n",
        "average_letter = score_to_letter(average)\n",
        "\n",
        "with open(\"grade_report.txt\", \"w\") as file:\n",
        "    file.write(f\"{'Name':<15}{'Score':<10}{'Grade':<10}\\n\")\n",
        "\n",
        "    for name, score, letter in students:\n",
        "        file.write(f\"{name:<15}{score:<10.2f}{letter:<10}\\n\")\n",
        "\n",
        "    file.write(\"\\n\")\n",
        "    file.write(f\"Class Average   {average:.2f}\\n\")\n",
        "    file.write(f\"Grade           {average_letter}\\n\")\n",
        "\n",
        "print(\"\\ngrade_report.txt has been created!\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"grade_report.txt\", \"r\") as file:\n",
        "    print(file.read())"
      ],
      "metadata": {
        "id": "YBf_auKDX1-f"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}