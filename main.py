import uvicorn
from decouple import config
from pyfiglet import print_figlet

from src.externals.infrastructures.api_config.api_config_infrastructure import (  # noqa: E501
    ApiConfigInfrastructure,
)
from src.externals.infrastructures.ioc_container_config.witch_doctor_container_config_infrastructure import (  # noqa: E501
    WitchDoctorContainerConfigInfrastructure,
)

if __name__ == '__main__':
    WitchDoctorContainerConfigInfrastructure.build_ioc_container()

    host = config('SERVER_HOST')
    root_path = config('ROOT_PATH')
    port = int(config('SERVER_PORT'))
    app = ApiConfigInfrastructure.start_app()

    print(f'Server is ready at URL {host}:{str(port) + root_path}')
    print_figlet(text='vermax-api', colors='0;78;225', width=200)

    uvicorn.run(app, host=host, port=port)
