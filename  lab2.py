{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOwzIX7Gd4W3JDQ7MNTZF7g",
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
        "<a href=\"https://colab.research.google.com/github/laa0025/cs104/blob/main/%20lab2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ubTthToh7Xpd"
      },
      "outputs": [],
      "source": [
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
        "    grade = float(input(f\"Enter {name}'s grade (0-100): \"))\n",
        "\n",
        "    while grade < 0 or grade > 100:\n",
        "        print(\"Grade must be between 0 and 100.\")\n",
        "        grade = float(input(f\"Enter {name}'s grade (0-100): \"))\n",
        "\n",
        "    students.append((name, grade))\n",
        "\n",
        "total = 0\n",
        "\n",
        "for name, grade in students:\n",
        "    total += grade\n",
        "\n",
        "average = total / len(students)\n",
        "\n",
        "if average >= 90:\n",
        "    letter_grade = \"A\"\n",
        "elif average >= 80:\n",
        "    letter_grade = \"B\"\n",
        "elif average >= 70:\n",
        "    letter_grade = \"C\"\n",
        "elif average >= 60:\n",
        "    letter_grade = \"D\"\n",
        "else:\n",
        "    letter_grade = \"F\"\n",
        "\n",
        "with open(\"grade_report.txt\", \"w\") as file:\n",
        "    for name, grade in students:\n",
        "        file.write(f\"{name:<15}{grade:>6.2f}\\n\")\n",
        "\n",
        "    file.write(\"\\n\")\n",
        "    file.write(f\"{'Class Average':<15}{average:>6.2f}\\n\")\n",
        "    file.write(f\"{'Grade':<15}{letter_grade:>6}\\n\")\n",
        "\n",
        "print(\"grade_report.txt has been created.\")"
      ]
    }
  ]
}