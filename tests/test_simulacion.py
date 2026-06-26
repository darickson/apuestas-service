import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.simulacion import simular_partido  # noqa: E402


def test_estructura_resultado():
    r = simular_partido(2.0, 3.0, 4.0)
    assert set(r.keys()) == {"marcador", "resultado", "goles"}
    assert set(r["marcador"].keys()) == {"local", "visita"}
    assert r["resultado"] in {"local", "empate", "visita"}
    assert isinstance(r["goles"], list)


def test_marcador_consistente_con_resultado():
    for _ in range(500):
        r = simular_partido(1.8, 3.5, 4.5)
        gl, gv = r["marcador"]["local"], r["marcador"]["visita"]
        esperado = "local" if gl > gv else "visita" if gv > gl else "empate"
        assert r["resultado"] == esperado, (gl, gv, r["resultado"])


def test_goles_coinciden_con_marcador():
    for _ in range(200):
        r = simular_partido(2.5, 3.2, 2.7)
        locales = sum(1 for g in r["goles"] if g["equipo"] == "local")
        visitas = sum(1 for g in r["goles"] if g["equipo"] == "visita")
        assert locales == r["marcador"]["local"]
        assert visitas == r["marcador"]["visita"]


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    fallos = 0
    for fn in fns:
        try:
            fn()
            print(f"PASS  {fn.__name__}")
        except AssertionError as e:
            fallos += 1
            print(f"FAIL  {fn.__name__}: {e}")
    print(f"\n{len(fns) - fallos}/{len(fns)} tests OK")
    sys.exit(1 if fallos else 0)
