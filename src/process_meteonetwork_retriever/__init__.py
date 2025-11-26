from dotenv import load_dotenv
load_dotenv()

from .meteonetwork import _MeteoNetworkRetriever
import importlib.util
if importlib.util.find_spec('pygeoapi') is not None:
    from .meteonetwork import MeteoNetworkRetrieverProcessor

from .main import run_meteonetwork_retriever
from .utils.strings import parse_event