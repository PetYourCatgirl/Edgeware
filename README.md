
# Edgeware

This is a fork of [PetitTournesol/Edgeware](https://github.com/PetitTournesol/Edgeware) - see the README there for resources, FAQ, changelog, 'how to use'

### Changes 

- `EdgeWare/resource` subdirectories `/img`, `/vid`, `/audio` are now searched recursively
  - (`/img/smile1.jpg` still works, but now `/img/smiles/smile1.jpg` also works)
  - Much easier to install and remove multiple packs
- New resource subdirectory `resource/wallpapers`
  - If `Rotate Wallpapers` is enabled, wallpaper will be set to something in this folder (search recursively)
  - Manually specifying each wallpaper in the config no longer has an effect
  - Default wallpaper remains unaffected by this change
- No longer adds desktop shortcuts on start
