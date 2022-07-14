package com.example.bluetooth_checkin;

import androidx.appcompat.app.AppCompatActivity;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.UUID;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class CommsActivity extends AppCompatActivity{

    public BluetoothAdapter BTAdapter = BluetoothAdapter.getDefaultAdapter();
    private static final String TAG = "CommsActivity";
    BluetoothSocket mmSocket;
    BluetoothDevice mmDevice;

    EditText editTextName;
    RadioGroup radioGroup;
    RadioButton radioButton;


    public class ConnectThread extends Thread {
        private ConnectThread(BluetoothDevice device) throws IOException {

            BluetoothSocket tmp = null;
            mmDevice = device;
            try {
                UUID uuid = UUID.fromString("94f39d29-7d6d-437d-973b-fba39e49d4ee");
                tmp = mmDevice.createRfcommSocketToServiceRecord(uuid);
            } catch (IOException e) {
                Log.e(TAG, "Socket's create() khởi tạo không thành công!", e);
            }
            mmSocket = tmp;
            BTAdapter.cancelDiscovery();
            try {
                mmSocket.connect();
            } catch (IOException connectException) {
                Log.v(TAG, "Lỗi kết nối!");
                try {
                    mmSocket.close();
                } catch (IOException closeException) {

                }
            }
            send();
        }

        //Gửi message tới server Raspberry
        public void send() throws IOException {
            String msg = editTextName.getText().toString() + "#" + radioButton.getText();
            OutputStream mmOutputStream = mmSocket.getOutputStream();
            mmOutputStream.write(msg.getBytes());
            receive();
        }

        public void receive() throws IOException {
            InputStream mmInputStream = mmSocket.getInputStream();
            //tao mang byte 1024 bytes
            byte[] buffer = new byte[1024];
            int bytes;

            try {
                bytes = mmInputStream.read(buffer);
                String readMessage = new String(buffer, 0, bytes);
                Log.d(TAG, "Nội dung nhận: " + readMessage);
                TextView content = (TextView) findViewById(R.id.Datatl);
                //Hiển thị nội dung ra màn hình
                content.setText(readMessage );
                mmSocket.close();
            } catch (IOException e) {
                Log.e(TAG, "Lỗi nhận nội dung!");
                return;
            }
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_comms);

        editTextName = (EditText)findViewById(R.id.editTextName);

        BluetoothAdapter mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        final Intent intent = getIntent();
        final String address = intent.getStringExtra(MainActivity.EXTRA_ADDRESS);

        Button voltButton = (Button) findViewById(R.id.submitbt);
        radioGroup = findViewById(R.id.radioGroup);

        voltButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                final BluetoothDevice device = BTAdapter.getRemoteDevice(address);
                try {
                    new ConnectThread(device).start();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });

        if (!mBluetoothAdapter.isEnabled()) {
            Intent enableBluetooth = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            //Thuc hien viec mo bluetooth
            startActivityForResult(enableBluetooth, 0);
        }
    }

    @Override
    protected void onStop() {
        super.onStop();
        try {
            mmSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void checkButton(View v) {
        int radioId = radioGroup.getCheckedRadioButtonId();

        radioButton = findViewById(radioId);

        Toast.makeText(this, "Bạn đã chọn: " + radioButton.getText(),
                Toast.LENGTH_SHORT).show();
    }

}//close class