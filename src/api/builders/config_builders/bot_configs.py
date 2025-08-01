from uuid import UUID

from src.api.builders.config_builders.drone_configs import build_drone_config
from src.utils.configs.bot_configs import BotConfig
from src.utils.configs.bot_configs.server_config import ServerConfig
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.configs.model_configs.vehicle_configs.speeder_config import SpeederConfig


def build_bot_config(
    version: int,
    bot_name: str,
    bot_alias: str,
    owner_id: UUID,
) -> BotConfig:
    drone_config = build_drone_config(
        version=version,
        name=bot_name,
        alias=bot_alias,
    )
    return BotConfig(
        version=version,
        owner_id=owner_id,
        name=bot_name,
        alias=bot_alias,
        drone_config=drone_config
    )



def build_server_config(
    version: int,
    server_name: str,
    server_alias: str,
    owner_config: UserConfig,
    companion_config: DroneConfig
) -> ServerConfig:
    return ServerConfig(
        version=version,
        name=server_name,
        alias=server_alias,
        owner_config=owner_config,
        companion_config=companion_config,
    )


def build_speeder_config(
    version: int,
    speeder_name: str,
    speeder_alias: str,
    pilot_config: DroneConfig,
) -> SpeederConfig:
    return SpeederConfig(
        version=version,
        name=speeder_name,
        alias=speeder_alias,
        pilot_config=pilot_config
    )


