package com.example.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import com.facebook.AccessToken;
import com.facebook.CallbackManager;
import com.facebook.FacebookCallback;
import com.facebook.FacebookException;
import com.facebook.GraphRequest;
import com.facebook.GraphResponse;
import com.facebook.Profile;
import com.facebook.login.LoginResult;
import com.facebook.login.widget.LoginButton;

import org.json.JSONArray;
import org.json.JSONObject;

import java.nio.channels.InterruptibleChannel;
import java.util.Arrays;

public class MainActivity extends AppCompatActivity {

    CallbackManager manager;

    private static String email = "email";
    LoginButton fbLogin;
    TextView result;

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        manager.onActivityResult(requestCode, resultCode, data);
        super.onActivityResult(requestCode, resultCode, data);
        Toast.makeText(this, "Login success", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        manager = CallbackManager.Factory.create();

        fbLogin = (LoginButton)findViewById(R.id.login_button);
        //fbLogin.setReadPermissions(Arrays.asList(email));
        fbLogin.setReadPermissions(Arrays.asList(
                "public_profile", "email", "user_birthday", "user_friends"));

        result = (TextView)findViewById(R.id.response);

        fbLogin.registerCallback(manager, new FacebookCallback<LoginResult>() {
            @Override
            public void onSuccess(LoginResult loginResult) {
                GraphRequest request = GraphRequest.newMeRequest(loginResult.getAccessToken(),
                        new GraphRequest.GraphJSONObjectCallback() {
                            @Override
                            public void onCompleted(JSONObject object, GraphResponse response) {
                                try{
                                    JSONArray friends = object.getJSONObject("friendlists").getJSONArray("data");
                                    Log.d("FRIEND_CONT", friends.length() +"");
                                    for(int i = 0; i < 5; i++) {
                                        JSONObject friend = friends.getJSONObject(i);
                                        Log.d("FRIEND",  friend.getString("id"));
                                    }
                                }catch (Exception e){
                                    e.printStackTrace();
                                }
                            }
                        });

                request.executeAsync();

            }

            @Override
            public void onCancel() {
                result.setText("User cancelled login");
            }

            @Override
            public void onError(FacebookException error) {
                Log.d("FACEBOOK", error.toString());
            }
        });

    }
}
