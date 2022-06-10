
// valeur en millimètre
boitier_pile_hauteur = 16;
boitier_pile_longueur = 53;
boitier_pile_largeur = 26;
boitier_pile_emplacement_epaisseur = 2;

connecteur_edge_hauteur = 11.8;
connecteur_edge_longueur = 40;
connecteur_edge_largeur = 60 + 1; // was too small
connecteur_percage_bord_bas = 6;
connecteur_percage_bord_lat = 3;
connecteur_percage_diametre = 2;

microbit_largueur = 44;
microbit_longueur = 52;
microbit_hauteur = 9;

microbit_enfiche_connector = 7;

vibreur_boite_epaisseur = 2;
vibreur_largeur = 20;
vibreur_longueur = 20;
vibreur_hauteur = 13;
vibreur_oeil = 4;

boitier_epaisseur = 2; 
boitier_complet_largeur = connecteur_edge_largeur + (boitier_epaisseur * 2);
boitier_complet_longueur = connecteur_edge_longueur - microbit_enfiche_connector +  microbit_largueur + (boitier_epaisseur * 2);
boitier_complet_hauteur = 25 + (boitier_epaisseur * 2);

module fond() {
    difference() {
        cube([boitier_complet_largeur, boitier_complet_longueur, boitier_complet_hauteur]);
        translate([boitier_epaisseur, boitier_epaisseur, boitier_epaisseur])
            cube([boitier_complet_largeur - (boitier_epaisseur * 2),
                    boitier_complet_longueur- (boitier_epaisseur * 2),
                    boitier_complet_hauteur]);
        // trous sonores au fond
        translate([boitier_complet_largeur / 2, boitier_complet_longueur + 1 , boitier_complet_hauteur / 2])
            rotate([90,0,0])
            cylinder($fn=50, h=4, r=2);
        // autres trous sonores
        translate([boitier_complet_largeur / 2,
                    boitier_complet_longueur + 1,
                    boitier_complet_hauteur / 2])
        rotate([90,0,0])
            for (i = [0:5]) {
                translate([sin(360*i/6)*5,
                        cos(360*i/6)*5,
                        0])
                    cylinder($fn=50, h=4, r=1);
        }
        // trou USB + alimentation
        translate([boitier_complet_largeur / 2 - 25, boitier_complet_longueur - 3 , boitier_complet_hauteur - 6])
            // cube([15, 4, 7]);
            cube([32, 4, 7]);
    }
    // cube([boitier_complet_largeur, boitier_complet_longueur,boitier_epaisseur]);
}

module support_vibreur() {
    difference() {
        translate([boitier_complet_largeur / 2 - (vibreur_largeur / 2),
                boitier_epaisseur,  // + vibreur_boite_epaisseur,
                vibreur_boite_epaisseur])
                    color("red")
                        cube([vibreur_largeur + vibreur_boite_epaisseur,
                            vibreur_longueur + vibreur_boite_epaisseur,
                            vibreur_hauteur / 3]);
        translate([boitier_complet_largeur / 2 - (vibreur_largeur / 2) + vibreur_boite_epaisseur / 2, 
                boitier_epaisseur + 1,  // + vibreur_boite_epaisseur,
                vibreur_boite_epaisseur -1 ])
                        cube([vibreur_largeur,
                            vibreur_longueur,
                            vibreur_hauteur + 2]);
        // create vibreur oeils
        translate([boitier_complet_largeur / 2 - (vibreur_largeur / 2) + vibreur_boite_epaisseur / 2 - 2, 
                boitier_epaisseur - 1 + (vibreur_longueur / 2),
                vibreur_boite_epaisseur])
                        cube([vibreur_largeur + 4,
                            vibreur_oeil,
                            (vibreur_hauteur / 3) + 2]);
        
    }
    
//    translate([boitier_complet_largeur / 2 - (vibreur_largeur / 2), boitier_epaisseur + vibreur_boite_epaisseur,
//   boitier_epaisseur])
//        color("red")
//        cube([vibreur_largeur + vibreur_boite_epaisseur, vibreur_longueur + vibreur_boite_epaisseur, vibreur_hauteur]);
}

module support_boitier_pile() {
    difference() {
        translate([boitier_complet_largeur / 2 - (boitier_pile_longueur / 2) + boitier_epaisseur,
                    30 + boitier_epaisseur, // + boitier_pile_emplacement_epaisseur,
                    boitier_epaisseur])
            color("green")
                cube([boitier_pile_longueur + boitier_pile_emplacement_epaisseur,
                    boitier_pile_largeur + boitier_pile_emplacement_epaisseur,
                    boitier_pile_emplacement_epaisseur]);
        
        translate([boitier_complet_largeur / 2 - (boitier_pile_longueur / 2) + boitier_epaisseur +boitier_pile_emplacement_epaisseur / 2,
            30 + boitier_epaisseur + // boitier_pile_emplacement_epaisseur
                boitier_pile_emplacement_epaisseur / 2,
            boitier_epaisseur])
                cube([boitier_pile_longueur, // + boitier_pile_emplacement_epaisseur,
                    boitier_pile_largeur, // + boitier_pile_emplacement_epaisseur,
                    boitier_pile_emplacement_epaisseur + 1]);
    }
}

module support_connector_edge() {
    translate([connecteur_percage_bord_lat + boitier_epaisseur + 1, connecteur_percage_bord_bas + boitier_epaisseur, boitier_epaisseur])
        color("blue")
        cylinder(h=13, r=connecteur_percage_diametre + 2);
    translate([connecteur_percage_bord_lat + boitier_epaisseur + 54, connecteur_percage_bord_bas + boitier_epaisseur, boitier_epaisseur])
        color("blue")
        cylinder(h=13, r=connecteur_percage_diametre + 2);
}

module couvercle() {
    difference() {
        union() {
            translate([0, 0, boitier_complet_hauteur])
                color("orange")
                    cube([boitier_complet_largeur, boitier_complet_longueur, boitier_epaisseur]);
            difference() {
                translate([2, 2, boitier_complet_hauteur - 2])
                    color("yellow")
                        cube([boitier_complet_largeur - 4, boitier_complet_longueur - 4, boitier_epaisseur]);
                translate([1, 6, boitier_complet_hauteur - 2])
                    color("DarkCyan")
                        cube([boitier_complet_largeur , boitier_complet_longueur - 12, boitier_epaisseur]);
                translate([6, 1, boitier_complet_hauteur - 2])
                    color("DarkCyan")
                        cube([boitier_complet_largeur -12, boitier_complet_longueur, boitier_epaisseur]);

            }
        }
        translate([boitier_complet_largeur / 2 - 25 / 2,
                    connecteur_edge_longueur + 2,
                    boitier_complet_hauteur - 3])
            cube([25,  // largeur zone LED
                  22, // longueur zone LE,
                  boitier_epaisseur +  4]);
    }
}

union() {
    fond();
    support_vibreur();
    support_boitier_pile();
    support_connector_edge();
    //couvercle();
    //!couvercle();  // pour imprimer le couvercle
}
