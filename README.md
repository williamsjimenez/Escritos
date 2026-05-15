# Gestor documental Rectoría UNAL (GitHub Pages)

Aplicación web estática para gestión, lectura, edición y administración de documentos `.docx`.

## Despliegue
1. Suba el repositorio a GitHub.
2. En **Settings → Pages**, seleccione rama (`main`) y carpeta raíz (`/root`).
3. Abra la URL publicada.

## Estructura
Categorías requeridas: `efemerides`, `comunicados`, `discursos`, `correos`, `derechos_peticion`, `tweets`, `institucional`, `parrillas`, `efemerides_academicas`, `otros`.

Cada carpeta contiene:
- `metadata.json`
- archivos `.docx`

## Uso Rector
- Inicio: cards por categoría con indicadores por vencer/vencidos.
- Categoría: lectura, edición, descarga, WhatsApp, metadatos.
- Editor: Quill + exportación `.docx` con preservación de bloque institucional fijo.

## Uso Admin
- URL: `/admin/`
- Contraseña inicial: `UNAL-Rector-Admin-2026` (hash en `localStorage`).
- Configurar GitHub token en `/admin/config/` (owner, repo, branch, token).
- El token se almacena ofuscado localmente (XOR + Base64), no hardcodeado.

### Operaciones
- Subir documento + metadatos a carpeta y `metadata.json`.
- Editar metadatos inline en tabla.
- Eliminar documento + entrada metadata.
- Reemplazar versión conservando metadatos y fecha de actualización.
- Recalcular próximos a vencer (7 días) y vencidos.

## Validación institucional
- Encabezado/pie institucional visibles y protegidos en editor.
- En reemplazo admin se emite advertencia si no se detectan cadenas institucionales.

## Notas técnicas
- Librerías CDN: `mammoth.js`, `docx`, `quill`, `file-saver`.
- Integración GitHub REST API `/repos/{owner}/{repo}/contents/{path}` para PUT/DELETE.
