Wir entwickeln die Document Projection Architecture (DPA) für `vfi64/agentic-project-kit` im separaten privaten Architektur-Labor `vfi64/agentic-project-kit-dpa-lab`.

Arbeite ausschließlich aus dem aktuellen Remote-Repo und den dort dokumentierten Verträgen. Arbeite nicht aus Chat-Erinnerung.

## Verbindlicher Bootstrap

Lies zuerst vollständig und in genau dieser Reihenfolge:

1. `README.md`
2. `LAB_BOOTSTRAP.md`
3. `MAIN_REPOSITORY_CONTEXT.md`
4. `LAB_EXECUTION_CONTRACT.md`
5. `GOVERNANCE.md`
6. `STATUS.md`
7. `ROADMAP.md`
8. `DECISIONS.md`
9. `ASSUMPTIONS.md`
10. `specs/dpa/README.md`
11. `specs/dpa/DPA-000-VISION.md`
12. alle weiteren DPA-Dateien, die für die aktuelle Aufgabe relevant oder bereits `draft`, `review-ready` oder `stable` sind
13. `reviews/README.md`
14. relevante Einzel- und Konsolidierungsreviews
15. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
16. `integration/IMPORT_PLAN.md`

Beginne keinerlei fachliche Arbeit, bevor dieser Bootstrap vollständig gelesen ist.

## Autorität

Bei Widersprüchen gilt:

1. exakte Evidence aus dem realen `vfi64/agentic-project-kit` an einem konkreten Git-Ref,
2. `MAIN_REPOSITORY_CONTEXT.md`,
3. `LAB_EXECUTION_CONTRACT.md`,
4. akzeptierte Entscheidungen in `DECISIONS.md`,
5. normative DPA-Spezifikationen,
6. konsolidierte Reviews,
7. Einzelreviews,
8. Annahmen und Vorschläge,
9. Chat-Erinnerung.

Chat-Erinnerung ist niemals autoritativ.

## Aktueller Hauptrepo-Kontext

Der im Lab dokumentierte und belegte Ausgangsstand ist:

- Hauptrepo: `vfi64/agentic-project-kit`
- aufgezeichneter administrativer Main-Stand: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` (`Refresh handoff state after PR1863 (#1864)`)
- letzter aufgezeichneter substantieller Stand davor: `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d` (`Add post-L5 lifecycle audit evidence (#1863)`)
- Q2 hat den geplanten L5-Endpunkt erreicht; danach wurden Post-L5-Lifecycle-Evidence und Handoff-Refresh abgeschlossen.
- Die bestehende Dokumentenverwaltung im Hauptrepo umfasst bereits Registry, Lifecycle, Freshness/Drift, Sweep, Resolver, Evidence und Gate-Integration.
- Die DPA muss diese Mechanismen erweitern und darf kein paralleles System etablieren.
- Alle repo-spezifischen Details sind vor späterer Implementierung erneut gegen einen frischen `origin/main` zu prüfen.

Lies für Details und Einschränkungen zwingend `MAIN_REPOSITORY_CONTEXT.md`.

## Rolle des Labs

Das Lab ist:

- temporäres, versioniertes Architektur-Labor,
- keine Runtime-Abhängigkeit,
- keine Autorität für den aktuellen Runtime-Zustand des Hauptrepos,
- kein Ort für produktiven Kit-Code,
- kein zweites Direction-, Registry-, Lifecycle-, Freshness-, Evidence-, Workspace- oder Gate-System.

Nach erfolgreicher Validierung und Umsetzung leben die Runtime-Verträge ausschließlich im Hauptrepo.

## Statuskennzeichnungen

Kennzeichne oder behandle jede repo-spezifische Aussage als:

- `VERIFIED`
- `ASSUMPTION`
- `NORMATIVE`
- `PROPOSAL`
- `REJECTED`
- `NEEDS_MAIN_REPO_VALIDATION`

`VERIFIED` setzt einen exakten Ref und eine nachvollziehbare Evidence- oder Reproduktionsmethode voraus. Übereinstimmung mehrerer Modelle ist keine Evidence.

## Architektur-Leitentscheidung

Die DPA erweitert ausschließlich die bestehende Dokumentenverwaltung des Hauptrepos.

Bindende Invarianten:

- Canonical State besitzt keine Renderlogik.
- Renderer besitzen keine Schreiblogik.
- Renderer liefern ausschließlich Text oder Bytes.
- Lifecycle validiert, plant, sperrt und schreibt.
- Workflow-Orchestrierung serialisiert branch- und PR-übergreifend.
- Registry beschreibt Verträge, keine beliebigen Plugins.
- Renderer werden statisch und fail-loud aufgelöst.
- Ein Renderer berechnet genau ein registriertes Ziel und triggert keinen anderen Renderer.
- Evidence ist niemals Runtime-Autorität.
- Keine neue kanonische Historienquelle nur zur Vereinfachung einer Migration.
- Keine automatische Zusammenführung historischer Prosa bei Drift.
- Zeitablauf allein darf keinen harten FAIL verursachen.

Der vollständige Vertrag steht in `LAB_EXECUTION_CONTRACT.md`.

## Ziel

Erzeuge eine konsistente, RFC-ähnliche Spezifikationsserie DPA-000 bis DPA-900 mit:

- Vision und Architekturprinzipien,
- Terminologie,
- Dokumentmodell,
- Registry-/Lifecycle-Integration,
- Renderer-Vertrag,
- Freshness-/Gate-Vertrag,
- Concurrency- und Workflow-Serialisierung,
- Migration und Rollback,
- vollständiger DP1–DP5-Implementierungsspezifikation,
- Future-Scope,
- Entscheidungen,
- Diagrammen,
- Traceability,
- Review- und Importplanung.

Das Endprodukt ist keine Prompt-Sammlung.

## Arbeitsweise

- Deutsch, knapp, direkt und evidenzbasiert im Chat.
- Englisch in normativen Spezifikationen, Diagrammen und maschinenlesbaren Artefakten.
- Keine ungeprüften Behauptungen über den realen Hauptrepo-Zustand.
- Jede Architekturentscheidung mit Kontext, Alternativen, Begründung und Konsequenzen dokumentieren.
- Reviews von ChatGPT, Claude und Gemini separat speichern.
- Review-Aussagen erst nach Adjudikation in normative Dateien übernehmen.
- Traceability zwischen Motivation, Invarianten, Anforderungen, Entscheidungen, DP1–DP5, Tests, Gates, Evidence und Rollback herstellen.
- Änderungen in kohärenten, reviewbaren Commits vornehmen.
- Bei Phasen- oder Aufgabenwechsel `STATUS.md` aktualisieren.
- Bei Entscheidungsänderungen `DECISIONS.md` aktualisieren.
- Bei geänderter Faktenlage `ASSUMPTIONS.md` und gegebenenfalls `MAIN_REPOSITORY_CONTEXT.md` aktualisieren.
- Keine Routine-Rückfragen. Arbeite kontinuierlich weiter.

## Aktuelle Phase

Pre-adoption architecture phase, Phase A — Foundation.

Das Lab darf erst mit `agentic-project-kit` adoptiert werden, wenn DPA-000 bis mindestens DPA-500 stabil sind und die Governance-/Bootstrap-Verträge konsistent sind.

Bis dahin:

- keine `.agentic/`-Initialisierung,
- keine simulierte Kit-Adoption,
- kein produktiver Kit-Code.

## Erster Arbeitsauftrag

1. Prüfe nach dem Bootstrap die Lab-Grundstruktur und melde knapp:
   - Repo/Ref,
   - Phase,
   - normative Ausgangsdateien,
   - aktuelle Aufgabe,
   - offene Blocker,
   - verwendete Hauptrepo-Evidence,
   - `PROCEED` oder `STOP`.
2. Vervollständige `specs/dpa/DPA-000-VISION.md` zu einem vollständigen Vision- und Architekturprinzipienvertrag.
3. Erstelle `specs/dpa/DPA-100-FOUNDATIONS.md` mit verbindlicher Terminologie und Autoritätsbegriffen.
4. Lege erste Traceability-Artefakte an, ohne Implementierung als abgeschlossen darzustellen.
5. Erzeuge einen konsolidierten, commit-ref-bezogenen Review-Prompt für Claude Fable 5.
6. Pflege Entscheidungen, Annahmen und Status konsistent nach.
7. Committe die Arbeit in nachvollziehbaren, thematisch sauberen Einheiten.
8. Arbeite danach innerhalb Phase A ohne Routineunterbrechung weiter, bis deren Exit-Kriterien erfüllt sind oder ein echter Stoppgrund eintritt.

## Stopps

Stoppe und diagnostiziere präzise, wenn:

- ein benötigter Hauptrepo-Fakt nicht evidenzbasiert verfügbar ist,
- normative Dokumente widersprüchlich sind,
- eine Lösung ein paralleles Governance-System schaffen würde,
- eine neue Runtime-Wahrheitsquelle ohne akzeptierte Autorität eingeführt würde,
- Review-Prosa ohne Adjudikation normativ werden soll,
- produktiver Kit-Code in das Lab gelangen würde,
- eine Maintainer-Entscheidung zwingend erforderlich ist,
- die Aufgabe von einem ungelösten früheren DPA-Vertrag abhängt.

Andernfalls ohne Nachfragen fortfahren.
