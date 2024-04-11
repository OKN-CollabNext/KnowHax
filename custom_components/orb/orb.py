import reflex as rx


class Orb(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: rx.Var[str] = "https://prod.spline.design/Br2ec3WwuRGxEuij/scene.splinecode"
    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime"]