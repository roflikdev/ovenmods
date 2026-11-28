# Oven SMP client pack

Minecraft 1.21.1 / NeoForge 21.1.266. The `mods/` directory contains 56 pinned client mods; `resourcepacks/` contains Sodium translations and Oven's Russian translation supplement. `config/` carries the matching ModernFix compatibility settings. The launcher obtains the manifest from Oven API and verifies each file by SHA-256 before installing it.

The exact versions, upstream project links, licenses, and the Barehanded common-tag compatibility fix are recorded in `.github/pack-provenance/candidate.json`; resource pack provenance is in `.github/pack-provenance/resourcepacks.json`. The Russian supplement contains only keys missing from bundled mod translations, plus two reviewed corrections; its source JSON is `.github/pack-provenance/ru_ru_missing.json`. Create Deco and Create: The Air War have been removed. Client-only UI and rendering mods stay here; server-only optimization tools are in the private `oven-game` repository. The matching server set is version 1.3.13. The bundled `options.txt` sets Russian and enables both translation packs for new installations; the launcher enables both packs for existing players without replacing their other settings.

Run `python .github/pack-provenance/verify_ru.py` after changing mod versions to detect newly missing Russian strings and verify the resource pack hash.

Oven manager 1.3.8 settles inactive physical constructions before their first physics tick when possible. The client config hides Sable Ragdolls control hints; the game server enforces player-only ragdolls and automatic recovery.

Chat Heads shows player faces beside chat names. Controlling and Searchables improve keybind search. Tiny Item Animations was removed. The No Chat Reports client settings hide its chat controls and safety banner.
