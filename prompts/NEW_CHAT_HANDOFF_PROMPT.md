Wir entwickeln die Document Projection Architecture (DPA) für `vfi64/agentic-project-kit` im separaten Architektur-Labor `vfi64/agentic-project-kit-dpa-lab`.

Lies zuerst vollständig:

1. README.md
2. GOVERNANCE.md
3. STATUS.md
4. ROADMAP.md
5. DECISIONS.md
6. ASSUMPTIONS.md
7. specs/dpa/README.md
8. specs/dpa/DPA-000-VISION.md
9. reviews/README.md
10. integration/MAIN_REPO_VALIDATION_CHECKLIST.md
11. integration/IMPORT_PLAN.md

Leitentscheidung:

Die DPA erweitert ausschließlich die bestehende Dokumentenverwaltung des Hauptrepos. Sie darf kein paralleles Registry-, Lifecycle-, Freshness-, Evidence-, Workspace- oder Gate-System etablieren.

Das Lab ist:

- temporäres, versioniertes Architektur-Labor,
- keine Runtime-Abhängigkeit,
- keine Autorität für den aktuellen Zustand des Hauptrepos,
- kein Ort für produktiven Kit-Code.

Kennzeichne Aussagen als VERIFIED, ASSUMPTION, NORMATIVE, PROPOSAL, REJECTED oder NEEDS_MAIN_REPO_VALIDATION.

Ziel:

Erzeuge eine konsistente RFC-ähnliche Spezifikationsserie DPA-000 bis DPA-900. Reviews von ChatGPT, Claude und Gemini werden separat gespeichert und erst nach Konsolidierung in normative Spezifikationen übernommen.

Arbeitsweise:

- Deutsch, knapp und direkt im Chat.
- Englisch in Spezifikationen, Diagrammen und maschinenlesbaren Artefakten.
- Keine Aussagen über den realen Hauptrepo-Zustand ohne genaue Evidence.
- Keine Prompt-Sammlung als Endprodukt.
- Jede Architekturentscheidung begründen.
- Alternativen und verworfene Optionen dokumentieren.
- Traceability zwischen Anforderungen, Verträgen, DP1–DP5, Tests und Gates herstellen.
- Keine Routine-Rückfragen; arbeite kontinuierlich weiter.
- Stoppe nur bei echtem Architekturwiderspruch, fehlender zwingender Entscheidung oder nicht auflösbarer Quellenlage.

Erster Auftrag:

1. Prüfe die Lab-Grundstruktur auf Konsistenz.
2. Vervollständige DPA-000.
3. Erstelle DPA-100.
4. Lege eine erste Traceability-Struktur an.
5. Erzeuge einen konsolidierten Review-Prompt für Claude Fable 5.
6. Committe die Arbeiten nachvollziehbar im Lab-Repo.

Das Lab soll später mit dem agentic-project-kit adoptiert werden, aber erst nachdem DPA-000 bis mindestens DPA-500 stabil sind. Bis dahin keine `.agentic/`-Initialisierung vortäuschen.
