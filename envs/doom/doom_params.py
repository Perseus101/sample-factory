# noinspection PyUnusedLocal
def doom_override_defaults(env, parser):
    """RL params specific to Doom envs."""
    parser.set_defaults(
        encoder='convnet_simple',
        hidden_size=512,
        obs_subtract_mean=128.0,
        obs_scale=128.0,
        env_frameskip=4,
    )


# noinspection PyUnusedLocal
def add_doom_env_args(env, parser):
    p = parser

    p.add_argument('--num_agents', default=-1, type=int, help='Allows to set number of agents less than number of players, to allow humans to join the match. Default value (-1) means default number defined by the environment')
    p.add_argument('--num_humans', default=0, type=int, help='Meatbags want to play?')
    p.add_argument('--num_bots', default=-1, type=int, help='Add classic (non-neural) bots to the match. If default (-1) then use number of bots specified in env cfg')
