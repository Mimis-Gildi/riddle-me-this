# frozen_string_literal: true

module Jekyll

  # A Liquid filter that flattens nested variables in the given input string.
  #
  # @param input [String] a string that may contain nested Liquid variables
  # @return [String] the input string with all nested variables flattened
  module ExpandNestedVariableFilter

    # Flattens nested variables in the given input string.
    #
    # @param input [String] a string that may contain nested Liquid variables
    # @return [String] the input string with all nested variables flattened
    def flatten_up(input)
      Liquid::Template.parse(input).render(@context)
    end

  end

end

Liquid::Template.register_filter(Jekyll::ExpandNestedVariableFilter)
