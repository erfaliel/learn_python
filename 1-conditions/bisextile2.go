package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)         // génère un buffer d'entrée
	fmt.Print("Entrez une année : ")            // affiche le texte pour l'utilisateur
	annee_text, _ := reader.ReadString('\n')    // enregistre dans une varible le contenu du buffer quand on détecte \n
	annee_text = strings.Trim(annee_text, "\n") // Supprime le \n de la variable
	annee, _ := strconv.Atoi(annee_text)        // Convertit l'année du type string -> int

	if bisextile := annee%400 == 0 || (annee%4 == 0 && annee%100 != 0); bisextile {
		fmt.Printf("%d est une année bisextile \n", annee)
	} else {
		fmt.Printf("%d n'est pas une année bisextile \n", annee)
	}

}
