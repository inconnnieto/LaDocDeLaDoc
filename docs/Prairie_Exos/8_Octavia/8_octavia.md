# 8. Octavia

## Alpha

- **Le modèle des données en entrée et en sortie**

INPUT

longueur des lignes: comparison line A, B, C
reference line: Ref
answer given by participants: True/ False

OUTPUT
answers : true/ false

- **Le modèle du dataset d'entraînement**

length of lines: numerical values A, B, C, reference
answers by participants: true/ false

- **L’arbre qui, selon vous, permettrait de donner la bonne réponse à chaque fois**

```mermaid
flowchart TD
    A(Asch) --> B(Param ref, A, B, C, rep)
    B --> C(ref == A)
    C -->|Yes| D(rep == 1)
	    D -->|Yes| F(TRUE)
	    D -->|No| G(FALSE)
    
	  C -->|No| E(ref == B)
		  E -->|Yes| H(rep == 2)
				H -->|Yes| J(TRUE)
				H -->|No| K(FALSE)
				
		  E -->|No| I(ref == C)
			  I --> |Yes|L(rep == 3)
			  L --> |No|M
				  L --> |Yes|N(TRUE)
			  I --> |No|M(FALSE)
```

