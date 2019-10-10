/*服务定位器模式（Service Locator Pattern）用在我们想使用 JNDI 查询定位各种服务的时候。考虑到为某个服务查找 JNDI 的代价很高，服务定位器模式充分利用了缓存技术。在首次请求某个服务时，服务定位器在 JNDI 中查找服务，并缓存该服务对象。当再次请求相同的服务时，服务定位器会在它的缓存中查找，这样可以在很大程度上提高应用程序的性能。以下是这种设计模式的实体。

服务（Service） - 实际处理请求的服务。对这种服务的引用可以在 JNDI 服务器中查找到。
Context / 初始的 Context - JNDI Context 带有对要查找的服务的引用。
服务定位器（Service Locator） - 服务定位器是通过 JNDI 查找和缓存服务来获取服务的单点接触。
缓存（Cache） - 缓存存储服务的引用，以便复用它们。
客户端（Client） - Client 是通过 ServiceLocator 调用服务的对象。*/
import java.util.ArrayList;
import java.util.List;

public interface Service {
    public String getName();
    public void execute();
 }

 class Service1 implements Service {
    public void execute(){
       System.out.println("Executing Service1");
    }
  
    @Override
    public String getName() {
       return "Service1";
    }
 }
 class Service2 implements Service {
    public void execute(){
       System.out.println("Executing Service2");
    }
  
    @Override
    public String getName() {
       return "Service2";
    }
 }

 class InitialContext {
    public Object lookup(String jndiName){
       if(jndiName.equalsIgnoreCase("SERVICE1")){
          System.out.println("Looking up and creating a new Service1 object");
          return new Service1();
       }else if (jndiName.equalsIgnoreCase("SERVICE2")){
          System.out.println("Looking up and creating a new Service2 object");
          return new Service2();
       }
       return null;      
    }
 }

  
 class Cache {
  
    private List<Service> services;
  
    public Cache(){
       services = new ArrayList<Service>();
    }
  
    public Service getService(String serviceName){
       for (Service service : services) {
          if(service.getName().equalsIgnoreCase(serviceName)){
             System.out.println("Returning cached  "+serviceName+" object");
             return service;
          }
       }
       return null;
    }
  
    public void addService(Service newService){
       boolean exists = false;
       for (Service service : services) {
          if(service.getName().equalsIgnoreCase(newService.getName())){
             exists = true;
          }
       }
       if(!exists){
          services.add(newService);
       }
    }
 }

 class ServiceLocator {
    private static Cache cache;
  
    static {
       cache = new Cache();    
    }
  
    public static Service getService(String jndiName){
  
       Service service = cache.getService(jndiName);
  
       if(service != null){
          return service;
       }
  
       InitialContext context = new InitialContext();
       Service service1 = (Service)context.lookup(jndiName);
       cache.addService(service1);
       return service1;
    }
 }

 public class J2eeServiceLocatorPatternDemo {
    public static void main(String[] args) {
       Service service = ServiceLocator.getService("Service1");
       service.execute();
       service = ServiceLocator.getService("Service2");
       service.execute();
       service = ServiceLocator.getService("Service1");
       service.execute();
       service = ServiceLocator.getService("Service2");
       service.execute();      
    }
 }

 //j2ee 服务定位器模式