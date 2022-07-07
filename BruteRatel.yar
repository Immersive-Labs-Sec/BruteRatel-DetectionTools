rule BruteRatelConfig
{
    strings:
        $config_block = { 50 48 b8 [8] 50 68}
        $split_marker = { 50 48 b8 [8] 50 48 b8 }

    condition:
        filesize < 400KB and $config_block and #split_marker > 30
}