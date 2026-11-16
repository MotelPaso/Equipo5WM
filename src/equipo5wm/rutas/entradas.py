from fastapi import APIRouter, HTTPException, Path

from equipo5wm.classes import Entrada, Evento

CODIGO_DIGITOS = 20
CODIGO_MIN = 10 ** (CODIGO_DIGITOS - 1)
CODIGO_MAX = (10 ** CODIGO_DIGITOS) - 1

router = APIRouter(prefix="/entradas", tags=["entradas"])


def _buscar_evento(evento_id: int):
    return None


def _buscar_entrada(codigo: int):
    return None


def _hay_cupos(evento) -> bool:
    return False


@router.post("")
def crear_entrada(id: int):
    evento = _buscar_evento(id)
    if evento is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "EVENTO_NO_EXISTE", "evento_id": id},
        )
    if not _hay_cupos(evento):
        raise HTTPException(
            status_code=409,
            detail={"error": "SIN_CUPOS", "evento_id": id},
        )


@router.get("/eventos/{id}/resumen")
def resumen_entrada(id: int):
    evento = _buscar_evento(id)
    if evento is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "EVENTO_NO_EXISTE", "evento_id": id},
        )


@router.get("/{codigo}")
def get_entradas(
    codigo: int = Path(..., ge=CODIGO_MIN, le=CODIGO_MAX),
):
    entrada = _buscar_entrada(codigo)
    if entrada is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "ENTRADA_NO_EXISTE", "codigo": codigo},
        )


@router.post("/{codigo}/validar")
def validar_entrada(
    codigo: int = Path(..., ge=CODIGO_MIN, le=CODIGO_MAX),
):
    entrada = _buscar_entrada(codigo)
    if entrada is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "ENTRADA_NO_EXISTE", "codigo": codigo},
        )
    if entrada.estado == "UTILIZADA":
        raise HTTPException(
            status_code=409,
            detail={"error": "ENTRADA_UTILIZADA", "codigo": codigo},
        )
