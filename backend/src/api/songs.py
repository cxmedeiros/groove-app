from fastapi import APIRouter, HTTPException, Path, status
from src.db import database as db
from src.schemas.song import SongGet, SongModel, SongDelete,SongList
from starlette.responses import JSONResponse
from src.service.impl.song_service import SongService
from src.schemas.song import SongCreateModel

router = APIRouter()

# Get a specific song
@router.get(
    "/{song_id}",
    response_model=SongModel,
    response_class=JSONResponse,
    summary="Get a specific song",
)
def get_song(song_id: str):
    song_get_response = SongService.get_song(song_id)
    print("####################")
    print(song_get_response)
    return song_get_response

@router.get(
    "/",
    response_model=SongList,
    response_class=JSONResponse,
    description="Retrieve all songs"
)
def get_songs():
    songs = SongService.get_songs()
    return { 'songs': songs, }

@router.put(
    "/{song_id}",
    response_model=SongModel,
    response_class=JSONResponse,
    summary="update a song",
)
def edit_song(song_id: str, song: SongCreateModel):
    song_edit_response = SongService.edit_song(song_id, song)

    return song_edit_response

# Add a song
@router.post(
    "/create",
    response_model=SongModel,
    response_class=JSONResponse,
    summary="create a song",
)
def add_song(song: SongCreateModel):
    song_add_response = SongService.add_song(song)

    return song_add_response

@router.delete(
    "/{song_id}",
    response_model=SongDelete,
    response_class=JSONResponse,
    summary="delete a song",
)
def delete_song(song_id: str):
    song_delete_response = SongService.delete_song(song_id)
    return song_delete_response

@router.get(
    "/higlighted",
    response_model=SongList,
    response_class=JSONResponse,
    summary="get highlighted songs",
)
def get_highlighted():
    highlighted_response = SongService.get_highlighted()
    return {
        "musics": highlighted_response
    }

@router.get(
    "/songs_by_year/{year}",
    response_model=SongList,
    response_class=JSONResponse,
    summary="get all songs",
)
def get_by_year(year):
    song_get_response = SongService.get_by_year(year)

    return song_get_response

@router.get(
    "/songs_by_genre/{genre}",
    response_model=SongList,
    response_class=JSONResponse,
    summary="get all songs",
)
def get_by_genre(genre):
    song_get_response = SongService.get_by_genre(genre)

    return song_get_response

@router.get(
    "/songs_by_artist/{artist}",
    response_model=SongList,
    response_class=JSONResponse,
    summary="get all songs",
)
def get_by_artist(artist):
    song_get_response = SongService.get_by_artist(artist)

    return song_get_response

@router.get(
    "/songs_by_album/{album}",
    response_model=SongList,
    response_class=JSONResponse,
    summary="get all songs",
)
def get_by_album(album):
    song_get_response = SongService.get_by_album(album)

    return song_get_response


