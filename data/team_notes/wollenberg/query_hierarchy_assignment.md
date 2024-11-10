* Query
	* nicht zeitlich
		Informelles Suchintention
	* zeitlich
		* explizit zeitlich
			Suchen mit einer genauen Datumsangabe.
		* implizit zeitlich
			* historisches Ereignis
				Suchen mit einer Angaben eines Ereignis. zb. Wiedervereinigung, ...
			* aktuelles Ereignis
				Suchen nach Begebenheiten, die derzeit stattfinden. zb. Ukraine Krieg
			* zukünftiges Ereignis
				Suchen nach Begebenheiten, die noch nicht stattgefunden haben stattfinden werden/können. zb. Marslandung
			* wiederholendes Ereignis
				Suchen nach Begebenheiten, die periodisch wiederkommen. zb. Bundestagswahl
			* faktische Aktualität
				Suchen nach aktuellen Informationen die keine Interpretation zulassen. zb. Wetter, Aktienmarkt, ...

```
graph TD
    A[Query] --> B[Nicht zeitlich]
    A --> C[Zeitlich]
    
    B --> D[Informelle Suchintention]
    
    C --> E[Explizit zeitlich]
    C --> F[Implizit zeitlich]
    
    E --> G[Suchen mit einer genauen Datumsangabe]
    
    F --> H[Historisches Ereignis]
    F --> I[Aktuelles Ereignis]
    F --> J[Zukünftiges Ereignis]
    F --> K[Wiederholendes Ereignis]
    F --> L[Faktische Aktualität]
    
    H --> M[Suchen mit einer Angabe eines Ereignisses z.B. Wiedervereinigung]
    I --> N[Suchen nach derzeitigen Begebenheiten z.B. Ukraine Krieg]
    J --> O[Suchen nach zukünftigen Begebenheiten z.B. Marslandung]
    K --> P[Suchen nach periodisch wiederkehrenden Begebenheiten z.B. Bundestagswahl]
    L --> Q[Suchen nach aktuellen Informationen ohne Interpretationsspielraum z.B. Wetter, Aktienmarkt]
```
