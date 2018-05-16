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

	var bisextile bool

	// Evalue si année bisextile (sortie: booléen)
	switch {

	case (annee % 4) != 0:
		bisextile = false
	case (annee % 100) != 0:
		bisextile = true
	case (annee % 400) == 0:
		bisextile = true
	default:
		bisextile = false
	}
	// Affichage pour l'utilisateur
	if bisextile == true {
		fmt.Printf("%d est une année bisextile \n", annee)
	} else if bisextile == false {
		fmt.Printf("%d n'est pas une année bisextile \n", annee)
	} else {
		fmt.Println("Tu as encore du debug à faire mon gars…\n")
	}
}
