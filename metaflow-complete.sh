# Metaflow CLI bash completion handler
_metaflow_completion() {
    local IFS=$'\n'
    COMPREPLY=( $(
        env COMP_WORDS="${COMP_WORDS[*]}" \
            COMP_CWORD=$COMP_CWORD \
            _METAFLOW_COMPLETE=complete $1
    ) )
    return 0
}

# Registers the completion function with bash, enabling nosort for bash 4.4+
_metaflow_completion_setup() {
    local COMPLETION_OPTIONS=""
    local BASH_VERSION_ARR=(${BASH_VERSION//./ })

    # nosort option is only available in bash 4.4 and later
    if [ ${BASH_VERSION_ARR[0]} -gt 4 ] || \
       ([ ${BASH_VERSION_ARR[0]} -eq 4 ] && [ ${BASH_VERSION_ARR[1]} -ge 4 ]); then
        COMPLETION_OPTIONS="-o nosort"
    fi

    complete $COMPLETION_OPTIONS -F _metaflow_completion metaflow
}

# Run setup on shell init
_metaflow_completion_setup
