require_relative 'mp/version'

program :name 'mp'
program :version, Mp::VERSION
program :description, 'CLI for IMDB, basically.'

command :year do |c|
	c.syntax = 'mp year frozen'
	c.description = 'Returns release year'
	c.action do |args, options|
		puts 'TODO YEAR'
	end
end
