package main

import (
	"fmt"
	"strings"
)

func main() {

	// Paramètre du nombre de coup avant que je joeur ne perde
count := 12

// Liste des mots à trouver, proposés par le jeu.
var game_list []string
game_list = [
	"nez",
	"jet",
	"jeu",
	"zoo",
	"fer",
	"dos",
	"riz",
	"tir",
	"emu",
	"abus",
	"ados",
	"banc",
	"bile",
	"brut",
	"brai",
	"chat",
	"demo",
	"deco",
	"dodu",
	"aimer",
	"verge",
	"video",
	"vitre",
	"abusif",
	"boueux",
	"addittif",
	"adeptes",
	"abritais",
	"assomant"
]
	fmt.Println(count)
	fmt.Println(game_list)
}