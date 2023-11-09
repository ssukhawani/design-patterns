public class DbConnectionSingleton {
    private String url;
    private String username;
    private  String password;
    private static DbConnectionSingleton instance;

    // we will create the private constructor so that outside this class no one should be able to
    // instantiate this class
    private DbConnectionSingleton(String url, String username, String password){
        this.url = url;
        this.password = password;
        this.username = username;
    }

    @Override
    public String toString() {
        return "[ "+this.url + " - "+ this.username+ " - " + this.password+ " ]";
    }

    // we will define the public getInstance method to create only object of this class
    public static synchronized DbConnectionSingleton getInstance(){
        // i can not create the instance variable in this method scope because whenever this method will gets called
        // new variable will get added to stack with new object instead i can use class level instance variable
        // we will make that class level variable to static so that we can use that without creating new obj
        // will check if instance is not null then only will create, if instance already present we ll use that only
        if (instance == null) {
            // one more issue i found in this method is this is not thread safe if simultaneous threads
            // came in this method then this will create multiple objects which violates singleton
            // so making this method synchronized
            instance = new DbConnectionSingleton("https://db:120.0.01", "usename", "password");
        }
        return instance;
    }
}
