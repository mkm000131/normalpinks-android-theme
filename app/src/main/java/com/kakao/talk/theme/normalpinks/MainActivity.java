package com.kakao.talk.theme.normalpinks;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;

public class MainActivity extends Activity {
    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        try {
            Intent i = new Intent(Intent.ACTION_VIEW, Uri.parse("kakaotalk://settings/theme/" + getPackageName()));
            startActivity(i);
        } catch (Exception ignored) { }
        finish();
    }
}
