import configuration as cfg
import frontend.frontend as fe




def run_application():
    """Initializes and runs the application."""

    # Load configuration
    app_configuration = cfg.configure()

    # Run the application
    frontend = fe.initialize_frontend(app_configuration)
    fe.run_frontend(frontend)

run_application()