from pelican import signals

planets = {}

class PlanetFeedGenerator(object):
  def __init__(self, context, settings, path, theme, output_path, *null):
    self.context = context;
    self.settings = settings;

  def generate_output(self, writer):
    global planets

    for planet, arts in planets.iteritems():
      writer.write_feed(arts, self.context,
                        self.settings.get('PLANET_FEED_ATOM') % planet)

def get_generators(generators):
  return PlanetFeedGenerator

def get_articles(generator):
  global planets

  for art in generator.articles:
    if 'planets' in art.metadata:
      for p in [x.strip() for x in art.metadata['planets'].split(',')]:
        if not p in planets:
          planets[p] = [art]
        else:
          planets[p].append(art)

def register():
  signals.article_generator_finalized.connect(get_articles)
  signals.get_generators.connect(get_generators)
