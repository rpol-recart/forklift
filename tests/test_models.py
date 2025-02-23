from app.models import Loader, LoaderManager


def test_loader_create():
    '''
       Test create loader and setting init status
    '''
    loader_id = 'forklift1'
    loader = Loader(loader_id)

    assert loader.loader_id == loader_id
    assert loader.status is None


def test_update_loader_status():

    loader_id = 'forklift1'
    loader = Loader(loader_id)
    ts = loader.get_timestamp()
    assert ts > 0
    assert type(ts) is int
    loader.update_status('full')

    assert loader.status == 'full'
    assert loader.operation_time >= ts
    assert loader.operation_time <= ts+1

    ts = loader.get_timestamp()
    loader.update_status('empty')

    assert loader.status == 'empty'
    assert loader.operation_time >= ts
    assert loader.operation_time <= ts+1


def test_add_loaders():
    loader_manager = LoaderManager()
    loader_manager.add_loader('loader_001')
    loader_manager.add_loader('loader_002')

    assert len(loader_manager.loaders) == 2


def test_get_loaders():
    loader_manager = LoaderManager()
    loader_manager.add_loader('loader_001')
    loader_manager.add_loader('loader_002')

    loader = loader_manager.get_loader_by_id('loader_001')
    assert loader is not None
    assert loader.loader_id == 'loader_001'
    assert loader.status is None


def test_loaders_operations():
    loader_manager = LoaderManager()
    loader_manager.add_loader('loader_001')
    loader_manager.add_loader('loader_002')

    loader = loader_manager.get_loader_by_id('loader_001')
    loader.update_status('full')
    loader = loader_manager.get_loader_by_id('loader_002')
    loader.update_status('empty')

    loader = loader_manager.get_loader_by_id('loader_001')
    assert loader.status == 'full'
    assert loader.operation_time > 0

    loader = loader_manager.get_loader_by_id('loader_002')
    assert loader.status == 'empty'
    assert loader.operation_time > 0
