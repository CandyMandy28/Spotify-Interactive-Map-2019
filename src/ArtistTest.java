import com.wrapper.spotify.SpotifyApi;
import com.wrapper.spotify.exceptions.SpotifyWebApiException;
import com.wrapper.spotify.model_objects.specification.Artist;
import com.wrapper.spotify.requests.data.artists.GetArtistRequest;
import com.wrapper.spotify.requests.data.artists.GetArtistsAlbumsRequest;

import java.io.IOException;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

public class ArtistTest {
    //replace the accessToken with what you get from authorization.java
    private static final String accessToken = "banana";
    private static final String id = "0LcJLqbBmaGUft1e9Mm8HV"; //ABBA

    private static final SpotifyApi spotifyApi = new SpotifyApi.Builder()
            .setAccessToken(accessToken)
            .build();
    private static final GetArtistRequest getArtistRequest = spotifyApi.getArtist(id)
            .build();

    private static final GetArtistsAlbumsRequest getArtistsAlbumsRequest = spotifyApi.getArtistsAlbums(id)
            .album_type("appears-on")
            .limit(10)
            .offset(0)
            .build();

    public static void getArtist_Sync() {
        try {
            final Artist artist = getArtistRequest.execute();

            System.out.println("Name: " + artist.getName());
            System.out.println("Popularity: " + artist.getPopularity());
        } catch (IOException | SpotifyWebApiException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public static void getArtist_Async() {
        try {
            final Future<Artist> albumFuture = getArtistRequest.executeAsync();

            // ...

            final Artist artist = albumFuture.get();

            System.out.println("Name: " + artist.getName());
        } catch (InterruptedException | ExecutionException e) {
            System.out.println("Error: " + e.getCause().getMessage());
        }
    }

    public static void main(String[] args) {
        getArtist_Sync();
    }
}