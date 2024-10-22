# Entwicklung eines KI-gestützten Therapieempfehlungssystems

## Projektübersicht
- **Version**: Erste Testversion
- **Verwendetes LLM**: Claude 3.5 Sonnet
- **Codeherkunft**: 100% KI-generiert

## Entwicklungsprozess

### Phase 1: Initiale Entwicklung
**Initialer Prompt:**
```
Entwickle ein Therapie Empfehlungs System für Infektionskrankheiten. 
Verwende nur Informationen aus dem Leitfeiden. 
Externe Informationen wie Diagnose werden über externe Tools geliefert. 
Konzentriere dich auf die Therapiemepfehlung.
```
**Basis**: PDF-Version des ABS-Leitfades

### Identifizierte Probleme
- ❌ Keine Therapie nach Erreger Identifizierung
- ❌ Keine Möglichkeit zu Interagieren

### Phase 2: Erweiterungen
**Prompt 2:**
```
Es fehlt die Behandlung nachdem der Erreger festgestllt wurde
```
→ Implementation der erregerbasierte Therapie

**Prompt 3:**
```
Wie kann ich die Engine ausprobieren
```
→ Entwicklung einer CLI-Schnittstelle

## Status
✅ Funktionierendes System mit:
- Empirischer Therapieempfehlung
- Erregerbasierter Therapie
- Interaktiver Benutzeroberfläche